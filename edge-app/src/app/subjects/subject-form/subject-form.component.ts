import { Component, OnInit } from '@angular/core';

import { SubjectService } from '../shared/subject.service';
import { Discipline } from '../shared/discipline';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-subject-form',
  templateUrl: './subject-form.component.html',
  styleUrls: ['./subject-form.component.css']
})
export class SubjectFormComponent implements OnInit {

  title: string;
  discipline: Discipline = new Discipline();

  constructor(
    private subjectService: SubjectService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    var id = this.route.params.subscribe(params => {
      var id = params['id'];

      this.title = id ? 'Alterar Diciplina' : 'Nova Diciplina';

      if (!id)
        return;

      this.subjectService.getSubject(id)
        .subscribe(
          discipline => this.discipline = discipline,
          response => {});
    });
  }

  save() {
    var result;

    if (this.discipline.id){
      result = this.subjectService.updateSubject(this.discipline);
    } else {
      result = this.subjectService.addSubject(this.discipline);
    }
    result.subscribe(data => this.router.navigate(['/subjects']));
  }

}
