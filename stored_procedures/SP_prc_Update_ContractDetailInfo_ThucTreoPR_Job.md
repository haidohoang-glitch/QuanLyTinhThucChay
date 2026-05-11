# Stored Procedure: `prc_Update_ContractDetailInfo_ThucTreoPR_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-27 10:47:38.950000
- **Ngày sửa cuối**: 2019-05-27 10:47:38.950000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Hungnv
-- Create date: 
-- Description:	
-- =============================================
CREATE PROCEDURE [dbo].[prc_Update_ContractDetailInfo_ThucTreoPR_Job]
-- Add the parameters for the stored procedure here

AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    DECLARE @ngayThucHien DATE = GETDATE();

    -- Cap nhat thong tin phan bo tren bang ThucTreo_PR khi co su thay doi ben CONTRACT.dbo.CONTRACT_DETAILS
    EXECUTE [dbo].[prc_asd_ThucTreo_PR_Update_ContractDetailInfo] @NgayThucHien = @ngayThucHien;

    EXECUTE [dbo].[prc_brand_thuctreo_insert] @NgayThucHien = @ngayThucHien;


END;

```
