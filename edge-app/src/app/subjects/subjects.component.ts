import { Component, OnInit } from '@angular/core';

import { SubjectService } from './shared/subject.service';
import { Discipline } from './shared/discipline';

@Component({
  selector: 'app-subjects',
  templateUrl: './subjects.component.html',
  styleUrls: ['./subjects.component.css']
})
export class SubjectsComponent implements OnInit {

  private subjects: Discipline[] = [];

  constructor(private subjectService: SubjectService) { }

  ngOnInit() {
    this.subjectService.getSubjects()
      .subscribe(data => this.subjects = data);
  }

  deleteSubject(subjects) {
    if (confirm("Você tem certeza que quer deletar a disciplina " + subjects.name + "?")) {
      var index = this.subjects.indexOf(subjects);
      this.subjects.splice(index, 1);

      this.subjectService.deleteSubject(subjects.id)
        .subscribe(null);
    }
  }
}
