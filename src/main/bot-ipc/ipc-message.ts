export enum IPCMessageType {
    AGENT_RESPONSE = "agent-response",
    AGENT_QUERY = "agent-query"
}

export class IPCMessage {
    type: IPCMessageType
    body?: string

    constructor(type: IPCMessageType, body?: string) {
        this.type = type
        this.body = body
    }
}