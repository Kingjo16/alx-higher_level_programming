#include "lists.h"

/**
 * insert_node - this inserts a node at a given  uunumber.
 * @head: Pointer
 * @number: INSERTED NUMBER
 * Return: NULL for a functio fail and pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (temp == NULL || temp->n >= num)
	{
		new_node->next = temp;
		*current = new_node;
		return (new_node);
	}

	while (temp && temp->next && temp->next->n < num)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
