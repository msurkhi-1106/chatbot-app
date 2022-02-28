const { NlpManager } = require('node-nlp');

export class NlpService {
  manager = new NlpManager({ languages: ['en'] });

  constructor() {
    this.train();
  }

  async train() {
    this.manager.addDocument(
      'en',
      'Where did you go to school?',
      'question.school'
    );
    this.manager.addDocument('en', 'I have a tummy ache', 'illness.flu');
    this.manager.addDocument('en', 'I feel nauseous', 'illness.flu');

    this.manager.addAnswer('en', 'illness.flu', 'You have the stomach flu!');
    this.manager.addAnswer(
      'en',
      'question.school',
      'I studied medicine at the Alan Turing Virtual Institute of Medicine'
    );

    await this.manager.train();
    //this.manager.save();
  }
}
