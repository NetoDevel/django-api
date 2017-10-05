import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/catch';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class RegistryService {

  private url: string = "http://localhost:8000/api/v1/registry";

  constructor(private http: Http) { }

  addRegistryStudent(registry){
    return this.http.post(this.url, {'registry': registry})
      .map(res => res.json());
  }

}
