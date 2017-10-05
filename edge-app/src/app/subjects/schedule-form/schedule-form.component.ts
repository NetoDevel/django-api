import { Component, OnInit } from '@angular/core';

import { ScheduleService } from '../shared/schedule.service';
import { Schedule } from '../shared/schedule';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-schedule-form',
  templateUrl: './schedule-form.component.html',
  styleUrls: ['./schedule-form.component.css']
})
export class ScheduleFormComponent implements OnInit {

  title: string;
  schedule: Schedule = new Schedule();

  constructor(
    private scheduleService: ScheduleService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    var id = this.route.params.subscribe(params => {
      var id = params['id'];

      this.schedule.discipline_id = id;
      this.title = 'Novo horário'

      if (!id)
        return;
    });
  }

  save() {
    var result;

    console.log(this.schedule);

    result = this.scheduleService.addSchedule(this.schedule);

    result.subscribe(data => this.router.navigate(['/subjects']));
  }
}
