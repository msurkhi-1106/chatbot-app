export class User {
  name: string;
  typing: boolean = false;
  photo?: string;

  constructor(name: string, photo?: string) {
    this.name = name;
    this.photo = photo;
  }
}
