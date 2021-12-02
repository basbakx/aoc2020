void setup() {
 String[] lines = loadStrings("input.txt");
    for (int i = 0; i < lines.length; i++) {
      for(int j = 0; j < lines.length; j++){
        for(int k = 0; k < lines.length; k++){
          if(int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020){
            println(int(lines[i]) * int(lines[j]) * int(lines[k]));
          }
        }
      }
    }
  }


void draw() {
}