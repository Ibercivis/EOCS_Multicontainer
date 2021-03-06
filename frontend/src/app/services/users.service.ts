import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor(private httpClient: HttpClient) { }

  register(username): Observable<any> {
    let url = environment.microservices_url + ":9750/api/users/register?";
    let body = new URLSearchParams();
    body.set('name', username);
    url += body;
    return this.httpClient.post(url, JSON.stringify(body));
  }


  login(username): Observable<any> {
    let url = environment.microservices_url + ":9750/api/users/login?";
    let body = new URLSearchParams();
    body.set('name', username);
    url += body;
    return this.httpClient.post(url, JSON.stringify(body));
  }

  checkTokenAndGetUserId(token): Observable<any> {
    let url = environment.microservices_url + ":9750/api/users/token_test";
    let headers: HttpHeaders = new HttpHeaders();
    headers = headers.append('Authorization', token);
    return this.httpClient.get(url, { headers: headers });
  }

}
