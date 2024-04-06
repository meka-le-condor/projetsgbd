import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SuivievaluationComponent } from './suivievaluation.component';

describe('SuivievaluationComponent', () => {
  let component: SuivievaluationComponent;
  let fixture: ComponentFixture<SuivievaluationComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SuivievaluationComponent]
    });
    fixture = TestBed.createComponent(SuivievaluationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
