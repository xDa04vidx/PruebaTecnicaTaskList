import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { Task } from './app/task/task'; 

bootstrapApplication(Task, appConfig)  
  .catch((err) => console.error(err));
