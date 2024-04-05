import { Component, OnInit } from '@angular/core';
import { RouterOutlet,Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators,FormsModule, NgForm } from '@angular/forms';
import Swal from 'sweetalert2';
import axios from 'axios';
import { User ,Evaluation} from '../User';
import { NgForOf } from '@angular/common';
@Component({
  selector: 'app-enseignement',
  standalone: true,
  imports: [RouterOutlet,FormsModule,NgForOf],
  templateUrl: './enseignement.component.html',
  styleUrls: ['./enseignement.component.css']
})
export class EnseignementComponent implements OnInit{
            title='GEE';
            data: any;

            
            ngOnInit(): void {
              axios.get('http://localhost:3000/data')
              .then(response => {
                this.data = response.data.data;
               
              })
              .catch(error => {
                console.error(error);
              });
          }



}
   


