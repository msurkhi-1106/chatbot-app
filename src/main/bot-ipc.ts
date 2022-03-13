import fs from 'fs'
import { spawn, fork } from 'child_process'
import { v4 as uuidv4 } from 'uuid'
import { resolveBotPath } from './util'
import commandExists from 'command-exists'
import os from 'os'
import path from 'path'
import './ipc-cleanup'

export class BotIPC {
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
        let fifoRs = fs.createReadStream(null!, {fd})
        let fifoWs = fs.createWriteStream(path_w)
    
        console.log("Ready to write!")
        
        fifoWs.write("heyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyyheyyyyy")
        fifoRs.on("data", (b: Buffer) => {
            const data = b.toString('utf-8')
            console.log(data)
        })
    }
}