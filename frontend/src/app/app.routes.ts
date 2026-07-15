import { Routes } from '@angular/router';
import { Dashboard } from './pages/dashboard/dashboard';
import { Inbox } from './pages/inbox/inbox';
import { Cases } from './pages/cases/cases';
import { Deadlines } from './pages/deadlines/deadlines';
import { Dictations } from './pages/dictations/dictations';
import { Search } from './pages/search/search';

export const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: Dashboard },
  { path: 'inbox', component: Inbox },
  { path: 'cases', component: Cases },
  { path: 'deadlines', component: Deadlines },
  { path: 'dictations', component: Dictations },
  { path: 'search', component: Search }
]

