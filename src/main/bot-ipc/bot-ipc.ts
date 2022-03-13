import fs, { ReadStream, WriteStream } from 'fs'
import { spawn, fork } from 'child_process'
import { v4 as uuidv4 } from 'uuid'
import { resolveBotPath } from '../util'
import commandExists from 'command-exists'
import os from 'os'
import path from 'path'
import './ipc-cleanup'
import { IPCMessage, IPCMessageType } from './ipc-message'

export class BotIPC {
    fifoWs?: WriteStream
    fifoRs?: ReadStream
    callbackTable: {[id: string]: (response: IPCMessage) => void | boolean} = {}

    constructor() {}

    async spawnPython(path_r: string, path_w: string) {
        console.log(path_r)
        console.log(path_w)
        console.log(resolveBotPath('bot.py'))

        let pythonPath
        if(await commandExists('python3')) {
            pythonPath = 'python3'
        } else if(await commandExists('python')) {
            console.log("'python3' not found in PATH... trying 'python'")
            pythonPath = 'python'
        } else {
            throw new Error('Python was not found in $PATH!  Please check that python3 is installed')
        }

        const botScript = spawn(pythonPath, [resolveBotPath('bot.py'), path_w, path_r])
        console.log("spawned bot")
        botScript.stdout?.on("data", (data: Buffer) => {
            console.log("[Python3] " + data.toString('utf-8'))
        })
        botScript.stderr.on("data", (data: Buffer) => {
            console.log("[Python3] " + data.toString('utf-8'))
        })
    }

    async spawn(path_r = uuidv4(), path_w = uuidv4()) {
        path_r = path.resolve(os.tmpdir(), path_r)
        path_w = path.resolve(os.tmpdir(), path_w)

        const fifo_r = spawn('mkfifo', [path_r])
        const fifo_w = spawn('mkfifo', [path_w])

        await Promise.all([fifo_r, fifo_w].map(p => new Promise<void>((resolve, reject) => {
            p.on("exit", (code) => {
                if(code == 0) resolve()
                else reject()
            })
        })))

        console.log('Created read/write pipes')

        this.spawnPython(path_r, path_w)
    
        const fd = fs.openSync(path_r, 'r+')
        this.fifoRs = fs.createReadStream(null!, {fd})
        this.fifoWs = fs.createWriteStream(path_w)
    
        console.log("Ready to write!")
        
        this.fifoRs.on("data", (b: Buffer) => {
            const message: IPCMessage = JSON.parse(b.toString('utf-8'))
            this.processMessage(message)
        })
    }

    sendMessage(type: IPCMessageType, body?: string, responseCallback?: (response: IPCMessage) => void | boolean) {
        const message = new IPCMessage(type, body)
        if(responseCallback) this.callbackTable[message.id] = responseCallback
        this.fifoWs?.write(JSON.stringify(message))
    }

    private processMessage(message: IPCMessage) {
        if (message.id in this.callbackTable) {
            const resp = this.callbackTable[message.id](message)
            if(!resp) delete this.callbackTable[message.id]
        } else {
            switch(message.type) {
                case IPCMessageType.AGENT_RESPONSE:
                    console.log(message.body!)
            }
        }
    }
}