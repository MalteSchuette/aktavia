import { Component, inject, OnInit } from '@angular/core';
import { JsonPipe } from '@angular/common';
import { CaseService } from '../../services/case.service';
import { Case } from '../../models/case'


@Component({
  selector: 'app-cases',
  imports: [JsonPipe],
  templateUrl: './cases.html',
  styleUrl: './cases.scss',
})
export class Cases implements OnInit{
  private CaseService = inject(CaseService);
  cases: Case [] = [];

  ngOnInit(): void {
    this.CaseService.getCases().subscribe(data => {
      this.cases = data;
    })
  }
}
