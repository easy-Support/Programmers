# 메뉴 리뉴얼
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72411

제출 날짜: 2021년 5월 4일

## 문제 설명
최소 2명 이상의 손님이 주문된 단품 메뉴로 코스요리 조합

## 문제 풀이
+ course 만큼 반복하고,
+ orders 만큼 반복하면서 course 원소인 코스 개수만큼 조합을 만듭니다.
+ collections.Counter를 이용해 많은 값이 있는 순서와 그 개수를 이용해 개수가 2 이상 그리고 개수가 가장 많은 단품 메뉴 조합을 가져옵니다.
