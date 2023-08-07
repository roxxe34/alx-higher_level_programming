#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 else
 */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *check = list;

	if (!list)
		return (0);

	while (curr && check && check->next)
	{
		curr = curr->next;
		check = check->next->next;
		if (curr == check)
			return (1);
	}

	return (0);
}
