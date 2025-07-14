from celery import shared_task
from .models import Listing


@shared_task
def update_listing_statistics():
    """Background task to update listing statistics."""
    total_listings = Listing.objects.count()
    print(f"Total listings: {total_listings}")
    return total_listings


@shared_task
def cleanup_old_listings():
    """Background task to cleanup old listings."""
    # This is a placeholder for cleanup logic
    print("Cleanup task executed")
    return "Cleanup completed" 