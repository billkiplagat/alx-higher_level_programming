#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: head
 * Return: 0 if no, 1 if yes
 */
int check_cycle(listint_t *list)
{
listint_t *fast, *slow = list;
if (list == NULL)
/* The list is empty or has only one node*/
return (0);
fast = list->next;
while (slow != NULL && fast != NULL && fast->next != NULL)
{
if (slow == fast)
return (1);
fast = fast->next->next;
slow = slow->next;
}
return (0);
}
