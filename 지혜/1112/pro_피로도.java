class Solution {
    static int answer = 0;
    public int solution(int k, int[][] dungeons) {
        
       boolean[] visited = new boolean[dungeons.length];
        dfs(dungeons, visited, k, 0);
        return answer;
    }
    public static void dfs(int[][]dungeons, boolean[] visited, int k, int count){
        answer = Math.max(answer, count);
        for(int i =0; i<dungeons.length; i++){
            if(!visited[i] && k>=dungeons[i][0]){
                visited[i] = true;
                dfs(dungeons, visited, k-dungeons[i][1] , count +1);
                visited[i] = false;
            }
        }
    }
}
