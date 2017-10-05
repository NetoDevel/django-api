import { Component, OnInit } from '@angular/core';

import { ScheduleService } from '../shared/schedule.service';
import { Schedule } from '../shared/schedule';
import { Router, ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css']
})
export class ScheduleComponent implements OnInit {

  private schedules: Schedule[] = [];

  constructor(
    private scheduleService: ScheduleService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    var id = this.route.params.subscribe(params => {
      var id = params['id'];

      if (!id)
        return;

      this.scheduleService.getSchedules(id)
        .subscribe(data => this.schedules = data);
    });
  }

}
