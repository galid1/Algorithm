package com.galid.algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// 백준 2376 단말 정점들의 거리
public class LeafNodesDistance {

    public static class BinaryTree {
        private Node root;

        /**
         *                                                                o
         *                                                              /   \
         * 1번은 단말노드여야 하며, 무조건 2개의 자식을 가져야하므로  o      o  모양으로 시작하게됨
         */
        public BinaryTree(){
            root = new Node(0, null);
            root.left = new Node(1, root); // 무조건 1번 단말 노드
            root.right = new Node(0, root);
        }

        /**
         * 조건 1 : 중위 순회시 탐색되는 단말노드 순서대로 번호가 매겨짐
         * 조건 2 : 자식노드 존재시 무조건 2개의 자식 모두 존재 아니면 아예 없음
         *
         * 거리가 0이 될때 까지 하나씩 줄이면서
         * 부모 노드로 이동함 이때 우->상 방향으로 이동했다면 우->하로 한번 이동함 (좌->상 이라면 계속 좌->상 으로 이동)
         * 그 후 좌->하로 이동하면서 양쪽 자식을 생성
         */
        public void createTree(List<Integer> distances) {
            Node start = this.root.left; // 1번 노드에서 시작해서 createTreeByDistance() 가 끝날때마다 전달되는 각 단말노드에서 시작
            int number = 2;

            for (int distance : distances) {
                start = createTreeByDistance(distance, start);
                start.value = number++;
            }
        }

        /**
         * 하나의 거리를 받아 트리를 그려나감
         * @param distance
         * @param start
         * @return 다음 시작 단말노드
         */
        private Node createTreeByDistance(int distance, Node start){
            // 좌상으로 이동할 때 까지만 반복하며 좌상으로 이동
            while (start == start.parent.right) {
                if (start.parent != null && distance > 0) {
                    start = start.parent;
                    distance--;
                }
            }

            // 우상 한번 우하 한번 이동
            if (start.parent != null && distance > 0) {
                start = start.parent;
                distance --;

                start = start.right;
                distance --;
            }

            // 양 자식을 생성하며 좌하로 이동
            while (distance > 0){
                start.left = new Node(0, start);
                start.right = new Node(0, start);

                start = start.left;
                distance --;
            }

            // 다음 시작 단말노드 전달
            return start;
        }

        /**
         * a와 b 단말노드간의 거리를 구함
         */
        public int calDistanceBetweenAwithB(int startNodeNum, int endNodeNum){
            int distance = 0;
            Queue<Node> queue = new LinkedList<>();
            Node startNode = findStartNode(startNodeNum);
            startNode.visit = true;
            queue.add(startNode);

            while(!queue.isEmpty()){
                Node cur = queue.poll();

                if(cur.value == endNodeNum){
                    distance = cur.distance;
                    break;
                }

                int nextDistance = cur.distance + 1;
                if(cur.left != null && cur.left.visit != true){
                    cur.left.distance = nextDistance;
                    queue.add(cur.left);
                    cur.left.visit = true;
                }
                if(cur.right != null && cur.right.visit != true){
                    cur.right.distance = nextDistance;
                    queue.add(cur.right);
                    cur.right.visit = true;
                }
                if(cur.parent != null && cur.parent.visit != true){
                    cur.parent.distance = nextDistance;
                    queue.add(cur.parent);
                    cur.parent.visit = true;
                }
            }

            return distance;
        }

        /**
         * dfs를 이용해서 시작정점을 구함
         */
        private Node findStartNode(int startNumber){
            Queue<Node> queue = new LinkedList<>();
            queue.add(this.root);
            this.root.visit = true;

            while(!queue.isEmpty()){
                Node cur = queue.poll();

                if (cur.value == startNumber) {
                    cleanVisit(this.root);
                    return cur;
                }

                if(cur.left != null && cur.left.visit == false) {
                    queue.add(cur.left);
                    cur.left.visit = true;
                }
                if(cur.right != null && cur.right.visit == false) {
                    queue.add(cur.right);
                    cur.right.visit = true;
                }
                if(cur.parent != null && cur.parent.visit == false){
                    queue.add(cur.parent);
                    cur.parent.visit = true;
                }
            }

            cleanVisit(this.root);
            return null;
        }

        /**
         * 방문 기록 초기화
         */
        private void cleanVisit(Node root){
            root.visit = false;
            if(root.left != null)
                cleanVisit(root.left);
            if(root.right != null)
                cleanVisit(root.right);
        }

        /**
         * 번호 매기기 (중위 순회하며 양 자식이 null인 경우 번호 부여) 해도 되지만 create하며 그냥 번호도 매김
         */
//    public void numbering(){
//    }

        public static class Node {
            int value;
            Node left;
            Node right;
            Node parent;
            boolean visit;
            int distance;

            public Node(int value, Node parent) {
                this.value = value;
                this.parent = parent;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));

        // 정보 입력
        int nodeCount = Integer.parseInt(bReader.readLine());
        List<Integer> distances = new ArrayList<>();
        for(int i = 0; i < nodeCount - 1; i++){
            distances.add(Integer.parseInt(bReader.readLine()));
        }
        String[] ab = bReader.readLine().split(" ");
        int startNodeNum = Integer.parseInt(ab[0]);
        int endNodeNum = Integer.parseInt(ab[1]);

        // 트리 생성
        BinaryTree bTree = new BinaryTree();
        bTree.createTree(distances);
        System.out.println(bTree.calDistanceBetweenAwithB(startNodeNum, endNodeNum));
    }
}
