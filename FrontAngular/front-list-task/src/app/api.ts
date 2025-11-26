// src/app/api.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'  // Esto asegura que el servicio esté disponible en toda la aplicación
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:8000/tasks/'; // URL de tu API

  constructor(private http: HttpClient) {}

  getTasks(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
