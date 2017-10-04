import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Alunos';
  students = [];
  student : any;

  addStudent() {
    this.students.push(this.student);
  }

}
