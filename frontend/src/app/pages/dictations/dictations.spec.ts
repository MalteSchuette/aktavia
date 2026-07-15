import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Dictations } from './dictations';

describe('Dictations', () => {
  let component: Dictations;
  let fixture: ComponentFixture<Dictations>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Dictations],
    }).compileComponents();

    fixture = TestBed.createComponent(Dictations);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
