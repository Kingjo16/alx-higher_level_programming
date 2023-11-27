#include "lists.h"

/**
 * check_cycle - THis checks ador the loop cycle
 * @list: this is the head for a liked list
 *
 * Description - it checks doe a loop
 * Return: 1 for cycle adn 0 for not success
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (!list)
	{
		return (0);
	}
	first = list;
	second = list->next;
	while (second && first && second->next)
	{
		if (first == second)
		{
			return (1);
		}
		first = first->next;
		second = second->next->next;
	}
	return (0);
}
