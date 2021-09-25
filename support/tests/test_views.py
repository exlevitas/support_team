import pytest
from support.models import Ticket, Comment


@pytest.mark.django_db
class TestTicketViews:
    def test_create_ticket(self, client) -> None:
        assert Ticket.objects.count() == 0
        response = client.post(
            "",
            {"title": "PyTest is good", "author":"TugarinZmey", "text":"lost my gold after using pytest"},
        )
        assert response.status_code == 201, response.data
        assert Ticket.objects.count() == 1

    def test_create_comment(self, client) -> None:
        assert Comment.objects.count() == 0
        response = client.post(
            "",
            {"name_comments": "Developer 228", "position_comment": "Junior", "text_comment": "Very good post bro! Link us!"},
        )
        assert response.status_code == 201, response.data
        assert Comment.objects.count() == 1