import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CahiertextComponent } from './cahiertext.component';

describe('CahiertextComponent', () => {
  let component: CahiertextComponent;
  let fixture: ComponentFixture<CahiertextComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CahiertextComponent]
    });
    fixture = TestBed.createComponent(CahiertextComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
