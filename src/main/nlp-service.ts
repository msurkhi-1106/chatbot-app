const { NlpManager } = require('node-nlp');
import fs from 'fs'
import { v4 as uuidv4 } from 'uuid'

export class NlpService {
  manager = new NlpManager({ languages: ['en'] });

  constructor() {
    this.train();
  }

  async train() {
    const file = fs.readFileSync("config/dataset.json")
    const questions = JSON.parse(file.toString())

    questions.forEach((category: {questions: string | string[], answers: string | string[]}) => {
        let uuid = uuidv4()
        
        if(category.questions instanceof String) category.questions = [questions]
        if(category.answers instanceof String) category.answers = [questions];

        (category.questions as string[]).forEach((question: string) => {
            this.manager.addDocument(
                'en',
                question,
                uuid
              );
              console.log(question)
        });
        (category.answers as string[]).forEach((answer: string) => {
            this.manager.addAnswer('en', uuid, answer);
        })
    })

    await this.manager.train();
  }
}
