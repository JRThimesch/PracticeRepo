// insertArtist.java

import java.sql.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Scanner;
public class insertArtist{
  public static void main(String args[]){
    Connection connection = null;
    try{
		
      // Step 1: Connect to the database server.
      String host = "cslab-db.cs.wichita.edu";
      int port = 3306;
      String database = "REDACTED";
      String user = "REDACTED";
      String password = "REDACTED";
      String url = String.format("jdbc:mariadb://%s:%s/%s?user=%s&password=%s", host, port, database, user, password);
    	System.out.println("Testing connection to database: " + database);
    	try {
    	    try (Connection con = DriverManager.getConnection(url)){
    		System.out.println("Successfully connected to database: " + database);
    	    }
    	} catch (Exception e){
    	    e.printStackTrace();
    	}
      connection = DriverManager.getConnection(url);
      
    // Step 2: input
	Statement stmt = connection.createStatement();
	
	System.out.println("Inserting into Artist table: ");
    System.out.println("Please type the name of the artist you would like to insert: ");
    Scanner scanner = new Scanner(System.in);
    String nameTemp = scanner.nextLine();
    
    
    // Step 3: insertion
	// artist_id auto increments, so you do not need to enter an ID 
    String cmd = "INSERT into Artist (artist_name) VALUES ('" + nameTemp + "')";
	
    try{
		stmt.executeUpdate(cmd);
		System.out.println("Insert successful");  
	} catch(Exception e){
		System.out.println("Insert failed, try again");
	}
      System.out.format("%n");
    }
    
    // leave
    
    catch(SQLException e)
    {
      e.printStackTrace();
    }
    finally
    {
      try
      {
        if(connection != null)
        connection.close();
      }
      catch(SQLException e)
      {
        e.printStackTrace();
      }
    }
  }
}

