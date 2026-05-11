# Stored Procedure: `Insert_DmThongTinHopDongBanInventory`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-03-30 17:11:23.403000
- **Ngày sửa cuối**: 2020-03-30 17:15:22.813000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec Insert_DmThongTinHopDongBanInventory 'QC5180220'
--select * from DmThongTinHopDongBanInventory WHERE SoHopDong = 'QC5210320'

CREATE PROCEDURE Insert_DmThongTinHopDongBanInventory
	-- Add the parameters for the stored procedure here
	@SoHopDong nvarchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	if not  EXISTS (SELECT SoHopDong FROM DmThongTinHopDongBanInventory WHERE SoHopDong = @SoHopDong)
	Begin
    -- Insert statements for procedure here
	INSERT INTO dbo.DmThongTinHopDongBanInventory
        ( HopDongREF ,
          SoHopDong ,
          NgayDanhSo ,
          DmNhanVienREF ,
          DmKhachHangREF ,
          HopDongChiTietREF ,
          DmSanPhamREF ,
          TenSanPham ,
          GhiChu ,
          CreatedAt ,
          CreatedBy ,
          LastModifiedAt ,
          LastModifiedBy ,
          RecordStatus ,
          DeletedStatus
        )
SELECT  HopDongID ,
          SoHopDong ,
          NgayDanhSoHopDong ,
          SysNhanVienREF ,
          DmKhachHangREF ,
          NULL HopDongChiTietREF ,
          NULL DmSanPhamREF ,
          NULL TenSanPham ,
          NULL GhiChu ,
          CreatedAt ,
         'asd' CreatedBy ,
           LastModifiedAt ,
          'asd' LastModifiedBy ,
          0 RecordStatus ,
          0 DeletedStatus
		  FROM HopDong WHERE SoHopDong =@SoHopDong
		  Print 'Done' 
		  End
		  else
		  begin
		    Print 'Not Done'
		  end
END

```
