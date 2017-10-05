import { Component, OnInit } from '@angular/core';

import { SubjectService } from '../shared/subject.service';
import { Discipline } from '../shared/discipline';
import { Student } from '../../students/shared/student';
import { Router, ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-list-students',
  templateUrl: './list-students.component.html',
  styleUrls: ['./list-students.component.css']
})
export class ListStudentsComponent implements OnInit {

  students: Student[] = [];

  constructor(
    private subjectService: SubjectService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    var id = this.route.params.subscribe(params => {
      var id = params['id'];

      if (!id)
        return;

      this.subjectService.getStudents(id)
        .subscribe(
          student => this.students = student,
          response => {});
    });
  }

}
