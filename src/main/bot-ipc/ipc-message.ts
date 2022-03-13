import { v4 as uuidv4 } from 'uuid'

export enum IPCMessageType {
    AGENT_RESPONSE = "agent-response",
    AGENT_QUERY = "agent-query"
}

export class IPCMessage {
    type: IPCMessageType
    body?: string
    id: string

    constructor(type: IPCMessageType, body?: string, id: string = uuidv4()) {
        this.type = type
        this.body = body
        this.id = id
    }
}