#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint - Reverses a linked list in place
 * @head: Pointer to a pointer pointing to the first node in the list
 * Return: Pointer to the first node in the new reversed list
 */

void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current_node = *head;
	listint_t *next_node = NULL;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = previous;
		previous = current_node;
		current_node = next_node;
	}

	*head = previous;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the linked list
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *temp = *head, *revers = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			revers = slow->next;
			break;
		}
		if (!fast->next)
		{
			revers = slow->next->next;
			break;
		}
		slow = slow->next;
	}

		reverse_listint(&revers);

		while (revers && temp)
		{
			if (temp->n == revers->n)
			{
				revers = revers->next;
				temp = temp->next;
			}
			else
				return (0);
		}
		if (!revers)
			return (1);
		return (0);
}
