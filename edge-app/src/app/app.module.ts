import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { StudentsComponent } from './students/students.component';
import { StudentFormComponent } from './students/student-form/student-form.component';
import { StudentService } from './students/shared/student.service';

import { routing } from './app.routing';
import { SubjectsComponent } from './subjects/subjects.component';
import { SubjectFormComponent } from './subjects/subject-form/subject-form.component';
import { SubjectService } from './subjects/shared/subject.service';

@NgModule({
  declarations: [
    AppComponent,
    StudentsComponent,
    StudentFormComponent,
    SubjectsComponent,
    SubjectFormComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    routing
  ],
  providers: [StudentService, SubjectService],
  bootstrap: [AppComponent]
})
export class AppModule { }
