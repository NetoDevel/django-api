import { Component, OnInit } from '@angular/core';

import { StudentService } from '../shared/student.service';
import { SubjectService } from '../../subjects/shared/subject.service';
import { RegistryService } from '../shared/registry.service';
import { Student } from '../shared/student';
import { Registry } from '../shared/registry';
import { Discipline } from '../../subjects/shared/discipline';

import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-registry',
  templateUrl: './registry.component.html',
  styleUrls: ['./registry.component.css']
})
export class RegistryComponent implements OnInit {

  students: Student[] = [];
  subjects: Discipline[] = [];
  registry: Registry = new Registry();

  constructor(
    private studentService: StudentService,
    private subjectService: SubjectService,
    private registryService: RegistryService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    this.studentService.getStudents()
      .subscribe(data => this.students = data);

    this.subjectService.getSubjects()
      .subscribe(data => this.subjects = data);
  }

  save() {
    this.registryService.addRegistryStudent(this.registry)
      .subscribe(data => this.router.navigate(['/']));
  }

}
