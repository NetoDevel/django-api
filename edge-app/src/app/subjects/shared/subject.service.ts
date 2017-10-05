import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/catch';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class SubjectService {

  private url: string = "http://localhost:8000/api/v1/subjects";

  constructor(private http: Http) { }

  getSubjects() {
    return this.http.get(this.url)
      .map(res => res.json());
  }

  getSubject(id){
    return this.http.get(this.url + '/' + id)
      .map(res => res.json());
  }

  addSubject(discipline){
    return this.http.post(this.url + '/', {'discipline': discipline})
      .map(res => res.json());
  }

  updateSubject(discipline){
    return this.http.put(this.url + '/' + discipline.id, {'discipline': discipline})
      .map(res => res.json());
  }

  deleteSubject(id){
    return this.http.delete(this.url + '/' + id)
      .map(res => res.json());
  }

}
