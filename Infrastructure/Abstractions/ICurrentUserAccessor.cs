namespace EmployeeHelper.Infrastructure.Abstractions;

public interface ICurrentUserAccessor
{
	string GetUserEmail();
}