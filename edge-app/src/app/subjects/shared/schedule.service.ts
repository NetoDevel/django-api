import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/catch';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class ScheduleService {

  private url: string = "http://localhost:8000/api/v1/subjects";

  constructor(private http: Http) { }

  getSchedules(id){
    return this.http.get(this.url + '/' + id + '/view_schedules')
      .map(res => res.json());
  }

  addSchedule(schedule){
    return this.http.post(this.url + '/add_schedule', {'schedule': schedule})
      .map(res => res.json());
  }

}
