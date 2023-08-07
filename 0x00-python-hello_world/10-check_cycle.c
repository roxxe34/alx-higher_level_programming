#include "list.h"
/**
 * check_cycle - function checks if a singly linked list has a cycle
 * @list: pointer to the beginning of the node
 * Return: 1 if there is a cycle, 0 else
 */
int check_cycle(listint_t *list)
{
listint_t *curr, *checker;
if(list == NULL || list->next == NULL)
	return (0);
curr = list;
checker = curr->next;
while(curr != NULL && checker->next != NULL
	&& checker->next->next != NULL)
{
if (current == check)
	return (1);
current = current->next;
check = check->next->next;
}
return (0);
}
