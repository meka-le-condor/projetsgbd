import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-enseignant',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './enseignant.component.html',
  styleUrl: './enseignant.component.css'
})
export class EnseignantComponent {
  title= 'Enseignant';
}
