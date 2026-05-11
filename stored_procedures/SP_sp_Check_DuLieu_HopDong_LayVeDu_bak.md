# Stored Procedure: `sp_Check_DuLieu_HopDong_LayVeDu_bak`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-11 11:59:00.793000
- **Ngày sửa cuối**: 2024-10-11 11:59:24.750000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_Check_DuLieu_HopDong_LayVeDu_bak] 
	-- Add the parameters for the stored procedure here
	--log by duongnt truoc khi sua store
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
---Kiểm tra dữ liệu Hopdong, Hopdongchitiet với ThoiGian = getdate() -1
select N'Dữ liệu hợp đồng' Bảng, convert(date,lastmodifiedat) as DayCall , max(lastmodifiedat) as MaxTimeCall, count(*) as SoBanGhi from Hopdong where convert(date,lastmodifiedat) =  convert(date,getdate()-1) 
group by convert(date,lastmodifiedat)
union all
select N'Dữ liệu hợp đồng chi tiết' Bảng, convert(date,lastmodifiedat) as DayCall ,max(lastmodifiedat) as MaxTimeCall,  count(*) as SoBanGhi from Hopdongchitiet where convert(date,lastmodifiedat) = convert(date,getdate()-1)
group by convert(date,lastmodifiedat)
union all
select N'Dữ liệu hợp đồng thay đổi' Bảng, convert(date,lastmodifiedat) as DayCall ,max(lastmodifiedat) as MaxTimeCall,  count(*) as SoBanGhi from Hopdongthaydoi where convert(date,lastmodifiedat) = convert(date,getdate()-1)
group by convert(date,lastmodifiedat)
union all
select N'Dữ liệu hợp đồng chi tiết thay đổi' Bảng, convert(date,lastmodifiedat) as DayCall ,max(lastmodifiedat) as MaxTimeCall,  count(*) as SoBanGhi from Hopdongchitietthaydoi where convert(date,lastmodifiedat) = convert(date,getdate()-1)
group by convert(date,lastmodifiedat)
END

```
