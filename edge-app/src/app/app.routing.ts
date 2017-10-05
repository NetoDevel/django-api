import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule }   from '@angular/router';

import { StudentsComponent } from './students/students.component';
import { StudentFormComponent } from './students/student-form/student-form.component';

import { SubjectsComponent } from './subjects/subjects.component';
import { SubjectFormComponent } from './subjects/subject-form/subject-form.component';

import { ScheduleFormComponent } from './subjects/schedule-form/schedule-form.component';
import { ScheduleComponent } from './subjects/schedule/schedule.component';

import { RegistryComponent } from './students/registry/registry.component';
import { ListSubjectsComponent } from './students/list-subjects/list-subjects.component';

import { ListStudentsComponent } from './subjects/list-students/list-students.component';

const appRoutes: Routes = [
  { path: '', pathMatch: 'full', component: StudentsComponent },
  { path: 'students/new', component: StudentFormComponent},
  { path: 'students/registry', component: RegistryComponent},
  { path: 'students/:id/subjects', component: ListSubjectsComponent},
  { path: 'students/:id', component: StudentFormComponent},
  { path: 'students/:id/edit', component: StudentFormComponent},

  { path: 'subjects', component: SubjectsComponent},
  { path: 'subjects/new', component: SubjectFormComponent},
  { path: 'subjects/:id', component: SubjectFormComponent},
  { path: 'subjects/:id/add_schedule', component: ScheduleFormComponent},
  { path: 'subjects/:id/view_schedules', component: ScheduleComponent},
  { path: 'subjects/:id/students', component: ListStudentsComponent},
  { path: 'subjects/:id/edit', component: SubjectFormComponent}
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
