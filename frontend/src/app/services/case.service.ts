import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Case } from '../models/case';

@Injectable({
    providedIn: 'root'
})
export class CaseService {
    private http = inject(HttpClient);
    private apiUrl = 'http://localhost:8000/api/cases/';

    getCases(): Observable<Case[]> {
        return this.http.get<Case[]>(this.apiUrl);
    }
}