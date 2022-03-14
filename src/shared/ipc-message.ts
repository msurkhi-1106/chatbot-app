import { v4 as uuidv4 } from 'uuid'

export enum IPCMessageType {
    AGENT_RESPONSE,
    AGENT_QUERY
}

export class IPCMessage<MessageBodyType = any> {
    type: IPCMessageType
    body?: MessageBodyType
    id: string

    constructor(type: IPCMessageType, body?: any, id: string = uuidv4().replaceAll(/[^0-9a-fA-F]/g, "")) {
        this.type = type
        this.body = body
        this.id = id
    }

    serialize() {
        const id = Buffer.from(this.id, "hex")

        const descriptor = new Uint8Array(2)
        descriptor[0] = 0b00000000 | this.type  // Highest bit indicates whether more packets exist (unused), lower bits indicate message type
        descriptor[1] = id.length // Indicates id buffer length

        const data = [descriptor, id]
        if(this.body) {
            data.push(Buffer.from(JSON.stringify(this.body), "utf-8"))
        }

        return Buffer.concat(data)
    }

    static deserialize<MessageBodyType>(data: Buffer) {
        const descriptor = data.slice(0, 2)
        const id = data.slice(2, 2+descriptor.at(1)!)
        const body = data.slice(2+descriptor.at(1)!)

        let bodyDecoded: string | undefined = body.toString("utf-8")
        if(bodyDecoded == "") bodyDecoded = undefined
        else bodyDecoded = JSON.parse(bodyDecoded)
        
        return new IPCMessage<MessageBodyType>(descriptor.at(0)! & 0b01111111, bodyDecoded, id.toString("hex"))
    }
}