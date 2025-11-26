import { Component, OnInit } from '@angular/core';
import { ApiService } from './api'; 

interface Task {
  id: number;
  title: string;
  description: string;
  create_date_task: string;
  finish_planned_date: string;
  real_finish_date: string;
  create_date: string;
  modificated_date: string;
  create_user: string;
  modificate_user: string;
}

@Component({
  selector: 'app-task',  
  templateUrl: './task.html',
  styleUrls: ['./task.css'],
})
export class Task implements OnInit {
  tasks: Task[] = []; 

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getTasks().subscribe((data: Task[]) => {
      this.tasks = data; 
    });
  }
}
