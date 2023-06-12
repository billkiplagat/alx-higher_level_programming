#include <stdio.h>
#include "lists.h"
/**
 * reverseList - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverseList(listint_t **head) {
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current) {
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head) {
listint_t *slow = *head, *fast = *head, *temp = *head, *mid = NULL;
if (*head == NULL || (*head)->next == NULL) {
return (1);
}
while (1) {
fast = fast->next->next;
if (!fast) {
mid = slow->next;
break;
}
if (!fast->next) {
mid = slow->next->next;
break;
}
slow = slow->next;
}
reverseList(&mid);
while (mid && temp) {
if (temp->n == mid->n) {
mid = mid->next;
temp = temp->next;
} else {
return (0);
}
}
if (!mid) {
return (1);
}
return (0);
}
