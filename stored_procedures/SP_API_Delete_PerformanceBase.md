# Stored Procedure: `API_Delete_PerformanceBase`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-09-13 17:46:11.603000
- **Ngày sửa cuối**: 2022-09-13 17:46:11.603000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@RequestKey` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE  PROCEDURE [dbo].[API_Delete_PerformanceBase]
	-- Add the parameters for the stored procedure here
	@RequestKey NVARCHAR(500)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	IF EXISTS (SELECT 1 FROM dbo.ThucChay_PerformanceBase_ThayDoi WHERE UPPER(Request_key) = UPPER(@RequestKey)
              AND ISNULL(DeletedStatus, 0) = 0 )
		BEGIN
			DECLARE @status INT;
			DECLARE @id BIGINT;

			SELECT @status = RecordStatus, @id = Id
			FROM dbo.ThucChay_PerformanceBase_ThayDoi
			WHERE UPPER(Request_key) = UPPER(@RequestKey) AND ISNULL(DeletedStatus, 0) = 0

			IF(ISNULL(@status, 0) = 0)
			BEGIN
				 UPDATE dbo.ThucChay_PerformanceBase_ThayDoi
				SET LastModifiedAt = GETDATE(),
					LastModifiedBy = 'API_SanPham',
					DeletedStatus = 1
				WHERE Id = @id;

				SELECT 1 AS Id;
			END ELSE 
			BEGIN
				/** da ghi nhan roi thi khong cho update */
				SELECT -1 AS Id;
			END
		END;
	ELSE
		SELECT 0 AS Id;
END

```
