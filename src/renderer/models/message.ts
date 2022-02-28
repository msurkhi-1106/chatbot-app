export default class Message {
  date: Date;
  name: string;
  message: string;

  constructor(date: Date, name: string, message: string) {
    this.date = date;
    this.name = name;
    this.message = message;
  }
}
