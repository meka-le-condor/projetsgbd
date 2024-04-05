
import {Component} from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import { RouterOutlet } from '@angular/router';
@Component({
  selector: 'app-acceuil',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule,MatIconModule,RouterOutlet],
  templateUrl: './acceuil.component.html',
  styleUrl: './acceuil.component.css'
})
export class AcceuilComponent {
  title = 'GEE';
}
