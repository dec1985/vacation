# Agents

This document describes the different types of agents and roles that interact with the vacation management system.

## User Agents

### Regular Users
- Can view their own vacation records
- Can track total vacation days taken
- Access through authenticated login

### Super Users (Administrators)
- Can view all user vacation records
- Can access summary reports for all users
- Can export vacation data to CSV format
- Can view detailed vacation information for specific users

## System Roles

### Authentication Agent
- Handles user login and authentication
- Manages session security
- Redirects unauthenticated users to login page

### Data Management Agent
- Processes vacation record storage and retrieval
- Handles vacation calculations and summaries
- Manages user data relationships

## Access Patterns

- All vacation-related operations require user authentication
- Administrative functions are restricted to super users only
- Individual users can only access their own vacation data
- System maintains data integrity through Django ORM