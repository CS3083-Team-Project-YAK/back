### **1. User Management**

#### Endpoints

1. **Register a User**

   - **POST** `/api/users/register`
   - **Input**:

     ```json
     {
       "full_name": "John Doe",
       "username": "johndoe",
       "email": "john@example.com",
       "password": "password123"
     }
     ```

   - **Output**:

     ```json
     {"message": "User registered successfully", "user_id": 1}
     ```

2. **Login a User**
   - **POST** `/api/users/login`
   - **Input**:

     ```json
     {
       "username": "johndoe",
       "password": "password123"
     }
     ```

   - **Output**:

     ```json
     {"token": "jwt-token", "user_id": 1}
     ```

3. **Get User Profile**
   - **GET** `/api/users/profile`
   - **Headers**: `Authorization: Bearer <jwt-token>`
   - **Output**:

     ```json
     {
       "user_id": 1,
       "username": "johndoe",
       "email": "john@example.com",
       "leagues": [
         {"league_id": 1, "league_name": "Super League"}
       ]
     }
     ```

4. **Update User Settings**
   - **PUT** `/api/users/settings`
   - **Input**:

     ```json
     {
       "profile_setting": {"favorite_sport": "basketball"}
     }
     ```

   - **Output**:

     ```json
     {"message": "Settings updated successfully"}
     ```

---

### **2. League Management**

#### Endpoints

1. **Create a League**
   - **POST** `/api/leagues`
   - **Input**:

     ```json
     {
       "league_name": "Super League",
       "league_type": "public",
       "max_teams": 10,
       "draft_date": "2024-12-10"
     }
     ```

   - **Output**:

     ```json
     {"league_id": 1, "message": "League created successfully"}
     ```

2. **Get Leagues**
   - **GET** `/api/leagues`
   - **Query Parameters**: `?type=public` or `?type=private`
   - **Output**:

     ```json
     [
       {"league_id": 1, "league_name": "Super League", "league_type": "public"},
       {"league_id": 2, "league_name": "Private League", "league_type": "private"}
     ]
     ```

3. **Edit League**
   - **PUT** `/api/leagues/{league_id}`
   - **Input**:

     ```json
     {
       "league_name": "Updated League Name"
     }
     ```

   - **Output**:

     ```json
     {"message": "League updated successfully"}
     ```

4. **Delete League**
   - **DELETE** `/api/leagues/{league_id}`
   - **Output**:

     ```json
     {"message": "League deleted successfully"}
     ```

---

### **3. Team Management**

#### Endpoints

1. **Create a Team**
   - **POST** `/api/teams`
   - **Input**:

     ```json
     {
       "league_id": 1,
       "team_name": "Dream Team"
     }
     ```

   - **Output**:

     return json of the team as get team.

2. **Get Teams in a League**
   - **GET** `/api/teams`
   - **Query Parameters**: `?league_id=1`
   - **Output**:

     ```json
     [
       {"team_id": 1, "team_name": "Dream Team", "owner": "johndoe", "points": 100, "status": "active"},
       {"team_id": 2, "team_name": "Super Squad", "owner": "janedoe", "points": 80, "status": "inactive"}
     ]
     ```

3. **Edit Team**
   - **PUT** `/api/teams/{team_id}`
   - **Input**:

     ```json
     {
       "team_name": "New Team Name"
     }
     ```

   - **Output**:

    return json of the team as get team.

4. **Delete Team**
   - **DELETE** `/api/teams/{team_id}`
   - **Output**:

     ```json
     {"message": "Team deleted successfully"}
     ```

---

### **4. Draft Management**

#### Endpoints

1. **Start a Draft**
   - **POST** `/api/drafts/{league_id}/start`
   - **Output**:

     ```json
     {"message": "Draft started successfully"}
     ```

2. **Make a Draft Pick**
   - **POST** `/api/drafts/{draft_id}/pick`
   - **Input**:

     ```json
     {
       "team_id": 1,
       "player_id": 2
     }
     ```

   - **Output**:

     ```json
     {"message": "Player drafted successfully"}
     ```

3. **View Draft Status**
   - **GET** `/api/drafts/{draft_id}`
   - **Output**:

     ```json
     {
       "draft_id": 1,
       "status": "in-progress",
       "picks": [
         {"team_id": 1, "player_id": 2, "timestamp": "2024-12-01T12:00:00"}
       ]
     }
     ```

---

### **5. Match Management**

#### Endpoints

1. **Get Match Schedule**
   - **GET** `/api/matches`
   - **Query Parameters**: `?league_id=1`
   - **Output**:

     ```json
     [
       {"match_id": 1, "team1": "Dream Team", "team2": "Super Squad", "date": "2024-12-05"}
     ]
     ```

2. **Submit Match Results**
   - **POST** `/api/matches/{match_id}/results`
   - **Input**:

     ```json
     {
       "winner_team_id": 1,
       "final_score": "75-68"
     }
     ```

   - **Output**:

     ```json
     {"message": "Match results submitted successfully"}
     ```

---

### **6. Player Management**

#### Endpoints

1. **Get Available Players**
   - **GET** `/api/players`
   - **Query Parameters**: `?league_id=1&status=available`
   - **Output**:

     ```json
     [
       {"player_id": 1, "name": "Player One", "sport": "basketball", "fantasy_points": 25.4},
       {"player_id": 2, "name": "Player Two", "sport": "basketball", "fantasy_points": 20.1}
     ]
     ```

2. **Add Player to Team**
   - **POST** `/api/teams/{team_id}/players`
   - **Input**:

     ```json
     {"player_id": 1}
     ```

   - **Output**:

     ```json
     {"message": "Player added to team successfully"}
     ```

3. **Remove Player from Team**
   - **DELETE** `/api/teams/{team_id}/players/{player_id}`
   - **Output**:

     ```json
     {"message": "Player removed from team successfully"}
     ```
